import sys

def post_travel(s, e, vals, p_vals):
    root = vals[s]
    p_vals.append(root)
    # in case no child, do noting
    if s != e:
        l, r = s + 1, e
        # in case only one child
        if vals[s] < vals[l] or vals[s] > vals[r]:
            post_travel(l, r, vals, p_vals)
        else:
        # in case has both children
            m = (l + r) // 2
            while l != r:
                if root > vals[m]:
                    l = m + 1
                else:
                    r = m
                m = (l + r) // 2
            # m is right_child_index
            post_travel(m, e, vals, p_vals)  # right child travel
            post_travel(s+1, m-1, vals, p_vals)  # left child travel

def main():
    vals = []
    p_vals = []
    lines = sys.stdin.readlines()
    for line in lines:
        vals.append(int(line))
    post_travel(0, len(vals) - 1, vals, p_vals)
    while p_vals:
        print(p_vals.pop())

if __name__ == "__main__":
    sys.setrecursionlimit(int(1e8))
    main()