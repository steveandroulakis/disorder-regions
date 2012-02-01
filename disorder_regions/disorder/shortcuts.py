def highlight_region(seq, start, end):
    highlight_start = '<span class="sequence_highlight">'
    highlight_end = '</span>'
    end = end + len(highlight_start)
    seq_region = seq[:start] + highlight_start + seq[start-1:]
    seq_region = seq_region[:end+1] + highlight_end + seq_region[end:]
    return str(seq_region)
    
def highlight_mutation(seq, position, mutated_aa):
    highlight_start = '<span class="sequence_mutation">'
    highlight_end = '</span>'    
    original_aa = seq[position-1]
    aa_change = original_aa + '>' + mutated_aa
    end = position + len(highlight_start) + len(aa_change)
    seq_change = seq[:position-1] + aa_change + seq[position:]
    seq_change = seq_change[:position-1] + highlight_start + seq_change[position-1:]
    seq_change = seq_change[:end-1] + highlight_end + seq_change[end:]
    return str(seq_change)