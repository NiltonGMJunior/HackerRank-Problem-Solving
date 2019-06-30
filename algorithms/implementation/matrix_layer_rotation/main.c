#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN(a, b) a <= b ? a : b

char *readline();
char *ltrim(char *);
char *rtrim(char *);
char **split_string(char *);

/*
    The following code worked properly for relatively small input matrices.
    According to HackerRank's judge, some large matrices produced the wrong output.
    Some of these large matrices output were compared with the results produced by this program.
    The comparison yielded no differences, and Iǜe failed to recognized the differences so far.
    It should be noted that, in the case of large matrices, it is possible that proccess was killed before finishing.
    There is no compilation or runtime error, and no timeout in the HackerRank website.

    Exploring alternative solutions in the Discussion page of the problem could yield better implementations of the algorithm.
 */

void copyMatrix(int **source_matrix, int **dest_matrix, int matrix_rows, int matrix_columns)
{
    for (int row = 0; row < matrix_rows; ++row)
        for (int col = 0; col < matrix_columns; ++col)
            dest_matrix[row][col] = source_matrix[row][col];
}

void verifyPointer(void *pter)
{
    if (!pter)
    {
        printf("FAILED TO ALLOCATE MEMORY. EXITING PROGRAM...\n");
        exit(-1);
    }
}

int **rotateLayer(int matrix_rows, int matrix_columns, int **matrix, int layer)
{
    //  Temporary rotation matrix.
    int **temp = (int **)(malloc(matrix_rows * sizeof(int *)));
    verifyPointer(temp);

    for (int row = 0; row < matrix_rows; ++row)
    {
        temp[row] = (int *)(malloc(matrix_columns * sizeof(int)));
        verifyPointer(temp[row]);
    }

    copyMatrix(matrix, temp, matrix_rows, matrix_columns);

    // Copy the elements in the leftmost column of the layer in their correct positions
    for (int row = layer + 1; row < matrix_rows - layer; ++row)
        temp[row][layer] = matrix[row - 1][layer];

    // Copy the elements in the bottom row of the layer in their correct positions
    for (int col = layer + 1; col < matrix_columns - layer; ++col)
        temp[matrix_rows - layer - 1][col] = matrix[matrix_rows - layer - 1][col - 1];

    // Copy the elements in the rightmost column of the layer in their correct positions
    for (int row = matrix_rows - layer - 2; row > layer - 1; --row)
        temp[row][matrix_columns - layer - 1] = matrix[row + 1][matrix_columns - layer - 1];

    // Copy the elements in the upper row of the layer in their correct positions
    for (int col = matrix_columns - layer - 2; col > layer - 1; --col)
        temp[layer][col] = matrix[layer][col + 1];

    // memcpy(matrix, temp, (matrix_rows * matrix_columns) * sizeof(int));
    return temp;
}

void printMatrix(int matrix_rows, int matrix_columns, int **matrix)
{
    for (int row = 0; row < matrix_rows; ++row)
    {
        for (int col = 0; col < matrix_columns; ++col)
            printf("%d ", matrix[row][col]);
        printf("\n");
    }
}

// Complete the matrixRotation function below.
void matrixRotation(int matrix_rows, int matrix_columns, int **matrix, int r)
{
    // Number of layers in the matrix.
    int num_layers = (1 + MIN(matrix_columns, matrix_rows)) / 2;

    // If the outter layer of the matrix is l = 0, the the number of elements in any given layer is: 2 * (n + m - 2 - 4 * l);

    // Rotating a layer with k elements r times is the same as rotating the k elements r % k times.

    int num_elements;
    for (int layer = 0; layer < num_layers; ++layer)
    {
        num_elements = 2 * (matrix_rows + matrix_columns - 2 - 4 * layer);
        for (int rotation = 0; rotation < r % num_elements; ++rotation)
            matrix = rotateLayer(matrix_rows, matrix_columns, matrix, layer);
    }

    printMatrix(matrix_rows, matrix_columns, matrix);
}

int main()
{
    char **mnr = split_string(rtrim(readline()));

    char *m_endptr;
    char *m_str = mnr[0];
    int m = strtol(m_str, &m_endptr, 10);

    if (m_endptr == m_str || *m_endptr != '\0')
    {
        exit(EXIT_FAILURE);
    }

    char *n_endptr;
    char *n_str = mnr[1];
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0')
    {
        exit(EXIT_FAILURE);
    }

    char *r_endptr;
    char *r_str = mnr[2];
    int r = strtol(r_str, &r_endptr, 10);

    if (r_endptr == r_str || *r_endptr != '\0')
    {
        exit(EXIT_FAILURE);
    }

    int **matrix = malloc(m * sizeof(int *));

    for (int i = 0; i < m; i++)
    {
        *(matrix + i) = malloc(n * (sizeof(int)));

        char **matrix_item_temp = split_string(rtrim(readline()));

        for (int j = 0; j < n; j++)
        {
            char *matrix_item_endptr;
            char *matrix_item_str = *(matrix_item_temp + j);
            int matrix_item = strtol(matrix_item_str, &matrix_item_endptr, 10);

            if (matrix_item_endptr == matrix_item_str || *matrix_item_endptr != '\0')
            {
                exit(EXIT_FAILURE);
            }

            *(*(matrix + i) + j) = matrix_item;
        }
    }

    int matrix_rows = m;
    int matrix_columns = n;

    matrixRotation(matrix_rows, matrix_columns, matrix, r);

    return 0;
}

char *readline()
{
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char *data = malloc(alloc_length);

    while (true)
    {
        char *cursor = data + data_length;
        char *line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line)
        {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n')
        {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data)
        {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n')
    {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data)
        {
            data = '\0';
        }
    }
    else
    {
        data = realloc(data, data_length + 1);

        if (!data)
        {
            data = '\0';
        }
        else
        {
            data[data_length] = '\0';
        }
    }

    return data;
}

char *ltrim(char *str)
{
    if (!str)
    {
        return '\0';
    }

    if (!*str)
    {
        return str;
    }

    while (*str != '\0' && isspace(*str))
    {
        str++;
    }

    return str;
}

char *rtrim(char *str)
{
    if (!str)
    {
        return '\0';
    }

    if (!*str)
    {
        return str;
    }

    char *end = str + strlen(str) - 1;

    while (end >= str && isspace(*end))
    {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char **split_string(char *str)
{
    char **splits = NULL;
    char *token = strtok(str, " ");

    int spaces = 0;

    while (token)
    {
        splits = realloc(splits, sizeof(char *) * ++spaces);

        if (!splits)
        {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
