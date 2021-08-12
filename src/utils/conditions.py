


def group_query(q):
    if q:
        if len(q)>2 or ("group" not in q.keys()):
            raise ValueError("You can only use the group query")
        if q["group"] not in ["gender","total","age"]:
            raise ValueError("Insert a valid group query: age, gender or total")
