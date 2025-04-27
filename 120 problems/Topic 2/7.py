haystack = "sadbutsad"
needle = "sad"

index = haystack.find(needle)
if index != -1:
    print(f"Needle found at index: {index}")
else:
    print("Needle not found")
