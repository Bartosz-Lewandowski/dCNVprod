import tempfile

import pytest


def pytest_configure():
    pytest.temp_dir = "temp_dir"


# Define a fixture for a sample fasta_file
@pytest.fixture
def sample_fasta_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        # Write DNA code with 'ACTG' and 'N' nucleotides
        temp_file.write(
            """>1 dna:chromosome chromosome:Sscrofa11.1:1:1:274330532:1 REF
                        GCTTAATTTTTGTCATTTCTCACCCCTGCTCTTGAGAGCTTTTGTTGATAATGTTGTTAT
                        TGCTTTCATTCTGCTTTTATTTTGTAAGCCCTGCACTCATTCATCGCTGTACCCGAATAT
                        GAGGTAAGGAGTGGTAAAGAAAGACTGGACATAAAAGAGGAATTAGCATGTGCACTCTTC
                        AGATATAAATGCCATCAGTATTTTCCTATTAAAATGAAGCTTGTTTTCATCTCAGTGGAA
                        ATCTGTGGCTAAAGTACAACAATAGTAATGATAATGGTGAGGCTGTTGTACTTCACATCT
                        ATAAAATCTTGCATCAATAATTTGGTGACGATTCCTTTGGGTAGGCCTACGTTTTCTGTC
                        AGAGACACAGGAATACTTTATAAATAAAATTGTTAATGTCTGTTGATCTTTTTTCATTGG
                        AAGAGGGTGACCAGTTTACCTTTTGAAAAAAAACTTTCCTAATTTGGGCTTTTTTTTTTT
                        TTTCCTTTTTAGGGCTGTACCCATGGCATATGAAAGTTCCTGTGCTAAGGGTTGATCAGA
                        GCTGCAGCTGCCAGCTTACGCTACAGCAACACCAGATCCAGTTGTATCTGTGGCCCTGCT"""
        )
        temp_file.flush()
        yield temp_file.name  # Provide the file name as the fixture v
