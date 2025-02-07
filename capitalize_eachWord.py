def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

# Test the function
print(to_jaden_case("how can mirrors be real if our eyes aren't real"))
