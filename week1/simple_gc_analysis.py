import numpy as np

def calculate_gc(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    total = len(sequence)
    return (gc_count / total) * 100 if total > 0 else 0

def detailed_gc_analysis(sequence, window_size=100):
    gc_contents = []
    for i in range(0, len(sequence), window_size):
        window = sequence[i:i+window_size]
        if len(window) >= window_size/2:  # Only consider windows with at least half the size
            gc_contents.append(calculate_gc(window))
    return gc_contents

print("GC Content Analysis:")
print("Dataset\tTotal GC%\tGC Range\tGC Std Dev")
print("-------\t---------\t--------\t----------")

for i in range(1, 5):
    contig_file = f"./week1/code/genome-assembly/data{i}_contigs.fasta"
    
    try:
        with open(contig_file, 'r') as f:
            content = f.read().split('>')
            sequences = [seq.split('\n', 1)[1].replace('\n', '') for seq in content if seq.strip()]
        
        if sequences:
            longest = max(sequences, key=len)
            total_gc = calculate_gc(longest)
            window_gc = detailed_gc_analysis(longest)
            
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
    except Exception as e:
        print(f"Error processing data{i}: {e}")
