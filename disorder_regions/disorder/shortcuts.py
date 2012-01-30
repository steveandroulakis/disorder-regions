def highlight_region(seq, start, end):
    highlight_start = '<span class="sequence_highlight">'
    highlight_end = '</span>'
    end = end + len(highlight_start)
    seq_region = seq[:start] + highlight_start + seq[start-1:]
    seq_region = seq_region[:end+1] + highlight_end + seq_region[end:]
    return str(seq_region)