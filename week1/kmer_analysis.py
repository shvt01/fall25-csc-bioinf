from collections import Counter
import math

def analyze_kmer_frequency(sequence, k=6):
    kmers = [sequence[i:i+k] for i in range(len(sequence)-k+1)]
    kmer_counts = Counter(kmers)
    total_kmers = len(kmers)
    
    # Calculate frequency of each k-mer
    kmer_freq = {kmer: count/total_kmers for kmer, count in kmer_counts.items()}
    
    # Get top 10 most frequent k-mers
    top_kmers = sorted(kmer_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Calculate mean and standard deviation
    frequencies = list(kmer_freq.values())
    mean_freq = sum(frequencies) / len(frequencies)
    variance = sum((x - mean_freq) ** 2 for x in frequencies) / len(frequencies)
    std_dev = math.sqrt(variance)
    
    return top_kmers, mean_freq, std_dev

print("K-mer frequency analysis (k=6):")
print("Dataset\tTop K-mers\t\tMean Freq\tStd Dev")
print("-------\t-----------\t\t---------\t-------")

for i in range(1, 5):
    contig_file = f"./week1/code/genome-assembly/data{i}_contigs.fasta"
    
    try:
        with open(contig_file, 'r') as f:
            content = f.read().split('>')
            sequences = [seq.split('\n', 1)[1].replace('\n', '') for seq in content if seq.strip()]
        
        if sequences:
            longest = max(sequences, key=len)
            top_kmers, mean_freq, std_dev = analyze_kmer_frequency(longest[:1000])
            
            top_kmer_str = ", ".join([f"{kmer}({freq:.4f})" for kmer, freq in top_kmers])
            print(f"data{i}\t{top_kmer_str[:40]}...\t{mean_freq:.6f}\t{std_dev:.6f}")
    except Exception as e:
        print(f"Error processing data{i}: {e}")
