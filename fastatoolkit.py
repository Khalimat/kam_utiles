from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from pathlib import Path

def make_fasta_from_seqs_list(AA_seqs, seqs_names,
                              file_name, file_dir):
    """
    Make a fasta file from lists of AA seqs and ids

    :param AA_seqs: list containing strings of AA sequences
    :param seqs_names: list containing strings of seq names
    :param fasta_name: str, file name
    """
    pre_fasta = []
    for seq, seq_name in zip(AA_seqs, seqs_names):
        iter_rec = SeqRecord(Seq(seq), id=seq_name)
        pre_fasta.append(iter_rec)
    output_path = Path(file_dir) / f'{file_name}.faa'
    SeqIO.write(pre_fasta, output_path, "fasta")

