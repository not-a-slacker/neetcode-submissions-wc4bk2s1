class Node {
    public:
        int val;
        vector<Node> neigh;

};
class Solution {
public:
    vector<vector<int>> prereqs;
    unordered_set<int> visited;

    bool dfs(int i)
    {
        if (visited.count(i))
        {
            return false;
        }
        visited.insert(i);
        bool no_cycle=true;
        for(int prereq : prereqs[i])
        {
            no_cycle=dfs(prereq);
            if (!no_cycle){
                return false;
            }
        }
        visited.erase(i);
        prereqs[i].clear();
        return no_cycle;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i=0;i<numCourses;i++)
        {
            prereqs.push_back({});
        }
        for (auto course_prereq : prerequisites)
        {
            prereqs[course_prereq[0]].push_back(course_prereq[1]);
        }
        for (int i=0;i<numCourses;i++)
        {
            if (!dfs(i))
            {
                return false;
            }
        }
        return true;

    }

        

};
