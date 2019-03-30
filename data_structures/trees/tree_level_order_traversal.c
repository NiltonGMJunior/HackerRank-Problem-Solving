#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

typedef struct queue {
    struct node **data;
    int capacity;
    int first;
    int last;
} queue;

struct node* insert(struct node* root, int data) {
		
	if(root == NULL) {
	
        struct node* node = (struct node*)malloc(sizeof(struct node));

        node->data = data;

        node->left = NULL;
        node->right = NULL;
        return node;
	  
	} else {
      
		struct node* cur;
		
		if(data <= root->data) {
            cur = insert(root->left, data);
            root->left = cur;
		} else {
            cur = insert(root->right, data);
            root->right = cur;
		}
	
		return root;
	}
}

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/

queue* create_queue(int capacity)
{
    queue *new_queue = (struct queue*) malloc(sizeof(queue));
    if (new_queue == NULL) 
    {
        return NULL;
    }
    new_queue->data = (struct node**) malloc(sizeof(struct node*) * capacity);
    if (new_queue->data == NULL) 
    {
        return NULL;
    }
    new_queue->capacity = capacity;
    new_queue->first = -1;
    new_queue->last = -1;
    return new_queue;
}

queue* enqueue(queue* queue, struct node* data)
{
    // Empty queue
    if (queue->first == -1) 
    {
        queue->first = 0;
        queue->last = 0;
        queue->data[0] = data;
    }
    // Full queue
    else if ((1 + queue->last) % queue->capacity == queue->first)
    {
        return NULL;
    }
    // Queue with spaces avaliable
    else
    {
        queue->last = (1 + queue->last) % queue->capacity;
        queue->data[queue->last] = data;
    }

    return queue;
}

struct node* dequeue(queue* queue)
{
    // Empty queue
    if (queue->first == -1) return NULL;

    struct node* output = queue->data[queue->first];
    // In case there is only one element in queue
    if (queue->first == queue->last)
    {
        // Modifies queue to show that it is now empty
        queue->first == -1;
        queue->last == -1;
    }
    else
    {
        // Changes the pointer to the first element
        queue->first = (1 + queue->first) % queue->capacity;
    }

    return output;
}

void free_queue(queue *queue)
{
    if (queue != NULL)
    {   
        struct node* temp = dequeue(queue);
        while (temp != NULL)
        {
            free(temp);
            temp = dequeue(queue);
        }
        free(queue);
    }
}

void levelOrder(struct node *root) {
    // Creates the queue that holds the nodes per level
    // Arbitrarilly large queue
    queue *queue = create_queue(500);
    struct node *current_node = root;
    while (current_node != NULL)
    {
        printf("%d ", current_node->data);
        if (current_node->left != NULL)
        {
            queue = enqueue(queue, current_node->left);
        }
        if (current_node->right != NULL)
        {
            queue = enqueue(queue, current_node->right);
        }
        current_node = dequeue(queue);
    }
    free_queue(queue);
}

int main() {

    queue *queue = create_queue(10);
    for (int i = 0; i < 10; ++i)
    {
        struct node node;
        node.data = i;
        node.left = NULL;
        node.right = NULL;
        queue = enqueue(queue, &node);
        if (queue != NULL)
        {
            printf("Enqueued %d\n", queue->data[queue->last]->data);
            printf("First position: %d\n", queue->first);
            printf("Last position: %d\n", queue->last);
        }
    }

    for (int i = 0; i < 11; ++i)
    {
        printf("First position: %d\n", queue->first);
        printf("Last position: %d\n", queue->last);
        struct node* node = dequeue(queue);
        if (node != NULL)
        {
            printf("Dequeued %d\n", node->data);
        }
    }
    // struct node* root = NULL;
    
    // int t;
    // int data;

    // scanf("%d", &t);

    // while(t-- > 0) {
    //     scanf("%d", &data);
    //     root = insert(root, data);
    // }
  
	// levelOrder(root);
    // return 0;
}
