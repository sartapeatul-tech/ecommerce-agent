from langsmith import traceable

@traceable
def test():
    return "hello"

test()