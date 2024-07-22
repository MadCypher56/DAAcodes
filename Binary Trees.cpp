#include <iostream>

using namespace std;

class node
{
public:
    int data;
    node *left;
    node *right;

    node(int d)
    {
        this->data = d;
        this->right = NULL;
        this->left = NULL;
    }
}

node *
buildTree(node *root)
{
    cour << "Enter node data:" << endl;
    int data;
    cin >> data;
    root = new node(data);

    if (data == -1)
    {
        return NULL;
    }

    cout <
}

int main()
{

    node *root = NULL;

    // Creating a Tree
    root = buildTree();

    return 0;
}