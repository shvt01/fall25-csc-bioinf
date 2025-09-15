from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import numpy as np

def detailed_gc_analysis(sequence, window_size=100):
    gc_contents = []
    for i in range(0, len(sequence), window_size):
        window = sequence[i:i+window_size]
        if len(window) >= window_size/2:  # Only consider windows with at least half the size
            gc_contents.append(gc_fraction(window) * 100)
    return gc_contents

print("GC Content Analysis:")
print("Dataset\tTotal GC%\tGC Range\tGC Std Dev")
print("-------\t---------\t--------\t----------")

for i in range(1, 5):
    contig_file = f"./week1/code/genome-assembly/data{i}_contigs.fasta"
    records = list(SeqIO.parse(contig_file, "fasta"))
    
    if records:
        longest = max(records, key=lambda x: len(x))
        total_gc = gc_fraction(longest.seq) * 100
        window_gc = detailed_gc_analysis(str(longest.seq))
        
        gc_min = min(window_gc) if window_gc else 0
        gc_max = max(window_gc) if window_gc else 0
        gc_std = np.std(window_gc) if window_gc else 0
        
        print(f"data{i}\t{total_gc:.2f}%\t({gc_min:.1f}-{gc_max:.1f})\t{gc_std:.2f}")
        
        # Classify based on GC content
        if total_gc < 40:
            print(f"  → Likely AT-rich organism (e.g., Plasmodium, some bacteria)")
        elif total_gc > 60:
            print(f"  → Likely GC-rich organism (e.g., Actinobacteria, some fungi)")
        else:
            print(f"  → Moderate GC content (common in many bacteria and eukaryotes)")
