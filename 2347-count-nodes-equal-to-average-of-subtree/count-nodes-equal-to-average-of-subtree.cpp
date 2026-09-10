class Solution {
public:
    int ans = 0;

    pair<int, int> dfs(TreeNode* root) {
        if (root == nullptr) {
            return {0, 0};
        }

        // Left subtree
        auto left = dfs(root->left);

        // Right subtree
        auto right = dfs(root->right);

        // Current subtree ka sum
        int sum = root->val + left.first + right.first;

        // Current subtree mein total nodes
        int count = 1 + left.second + right.second;

        // Floor division automatically integer division se ho jayegi
        int average = sum / count;

        if (root->val == average) {
            ans++;
        }

        return {sum, count};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};