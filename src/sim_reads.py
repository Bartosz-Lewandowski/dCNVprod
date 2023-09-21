import gc
from subprocess import call

import numpy as np
from Bio import SeqIO

from src.config import MODIFIED_FASTA_FILE_NAME, SIM_DATA_PATH


class SimReads:
    def __init__(
        self,
        cov: int,
        cpu: int = 10,
        model: str = "novaseq",
    ) -> None:
        gc.collect()
        models = ["novaseq", "hiseq", "miseq"]
        if model in models:
            self.model = model
        else:
            raise ValueError(f"Wrong type of model. Try one of{models}")
        self.model = model
        self.fasta_file = "/".join([SIM_DATA_PATH, MODIFIED_FASTA_FILE_NAME])
        self.read_len = self._get_read_length()
        self.cov = cov
        self.cpu = cpu
        self.pathout = SIM_DATA_PATH

    def sim_reads_genome(self) -> tuple[str, str]:
        chrs = np.array(
            [len(fasta.seq) for fasta in SeqIO.parse(open(self.fasta_file), "fasta")]
        )
        chrs_len = np.sum(chrs)
        N = self._calc_N_reads(chrs_len)
        return self.sim_reads_with_InSilicoSeq(N)

    def sim_reads_with_InSilicoSeq(self, N: int) -> tuple[str, str]:
        command = f"iss generate --model {self.model} --genomes {self.fasta_file} --n_reads {N} --cpus {self.cpu} --output {self.pathout}/{self.cov}"
        call(command, shell=True)
        return (
            f"{self.pathout}/{self.cov}_R1.fastq",
            f"{self.pathout}/{self.cov}_R2.fastq",
        )

    def _get_read_length(self) -> int:
        match self.model:
            case "novaseq":
                return 150
            case "hiseq":
                return 125
            case "miseq":
                return 300
        return 150

    def _calc_N_reads(self, chr_len: int) -> int:
        return round(chr_len / self.read_len) * self.cov
