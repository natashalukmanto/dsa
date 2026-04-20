def simplifyPath0(path: str) -> str:
    stack = path.split("/")
    res = []

    for i in stack:
        if res and i == "..":
            res.pop()
        elif not res and i == "..":
            continue
        elif i != "" and i != ".":
            res.append(i)

    return "/" + "/".join(res)


def simplifyPath(self, path: str) -> str:
    stack = []

    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif not p or p == ".":
            continue
        else:
            stack.append(p)

    return "/" + "/".join(stack)
