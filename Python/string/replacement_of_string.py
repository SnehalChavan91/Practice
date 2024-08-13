sample="The lyrics is not that much poor"
if "not" in sample and "poor" in sample:
    if sample.index("not")<sample.index("poor"):
        sample=sample.replace(sample[sample.index("not"):sample.index("poor")+4],"good")
print(sample)
