def parse_version(version_string: str) -> tuple[int, int, int]:
    """Parse 'MAJOR.MINOR.PATCH' into a tuple of ints (current version not robust)."""
    parts = version_string.split('.')
    #return int(parts[0]), int(parts[1]), int(parts[2])  # Fails on invalid formats

# --- START YOUR SOLUTION HERE ---
# Validate format and raise ValueError when invalid.
    if len(parts) != 3:
        raise ValueError("Invalid version format")
    
    version_nums = []
    for part in parts:
        part = part.strip()
        if not part.isdigit():
            raise ValueError("Invalid version format")
        if len(part) > 1 and part.startswith('0'):
            raise ValueError("Invalid version format")  # leading zeros
        if len(part) > 50:
            raise ValueError("Invalid version format")  # excessively long
        version_nums.append(int(part))


    return tuple(version_nums)
# --- END OF YOUR SOLUTION ---
