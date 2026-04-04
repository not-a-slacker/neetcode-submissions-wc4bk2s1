def build(node,nums,seg_tree,start,end):
    if start == end:
        print(f"node : {node}, start : {start}")
        seg_tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        print(f"node : {node}, mid : {mid}, start : {start}, end : {end}")
        build(2*node,nums,seg_tree,start,mid)
        build(2*node+1,nums,seg_tree,mid+1,end)
        seg_tree[node] = max(seg_tree[2*node],seg_tree[2*node + 1])

def query(node,nums,seg_tree,start,end,l,r):
    if l>end or r<start:
        return -10001
    if l<=start and r>=end:
        return seg_tree[node]
    mid = (start + end)//2
    max1 = query(2*node,nums,seg_tree,start,mid,l,r)
    max2 = query(2*node+1,nums,seg_tree,mid+1,end,l,r)
    return max(max1,max2)
    


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seg_tree = [-10001] * (4*len(nums)+6)
        build(1,nums,seg_tree,0,len(nums) - 1)
        max_list = []
        for i in range(len(nums)-k + 1):
            max_list.append(query(1,nums,seg_tree,0,len(nums) - 1,i,i+k-1))
        return max_list

        