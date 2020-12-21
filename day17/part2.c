#include <stdio.h>
#include <string.h>


#define START_SIZE 8
#define CYCLES 6
#define MAX (START_SIZE + CYCLES + 4)


// "center" initial coordinates so indexes will always be >= 0
static const int INITIAL_ZERO = (int) MAX / 2 - START_SIZE / 2;


typedef int grid_t[MAX][MAX][MAX][MAX];


void cycle(grid_t grid) {
    grid_t neighbor_counter = {0};
    int count;
    int nb_x, nb_y, nb_z, nb_w;

    for (int x = 0; x < MAX; x++)
    for (int y = 0; y < MAX; y++)
    for (int z = 0; z < MAX; z++)
    for (int w = 0; w < MAX; w++)
    if (grid[x][y][z][w])
        for (int dx = -1; dx < 2; dx++)
        for (int dy = -1; dy < 2; dy++)
        for (int dz = -1; dz < 2; dz++)
        for (int dw = -1; dw < 2; dw++) {
            if (dx == 0 && dy == 0 && dz == 0 && dw == 0)
                continue;
            nb_x = x + dx;
            nb_y = y + dy;
            nb_z = z + dz;
            nb_w = w + dw;
            neighbor_counter[nb_x][nb_y][nb_z][nb_w] += 1;
        }

    for (int x = 0; x < MAX; x++)
    for (int y = 0; y < MAX; y++)
    for (int z = 0; z < MAX; z++)
    for (int w = 0; w < MAX; w++) {
        count = neighbor_counter[x][y][z][w];
        if (grid[x][y][z][w]) {
            if (count == 2 || count == 3) {
                grid[x][y][z][w] = 1;
                continue;
            }
        } else if (count == 3) {
            grid[x][y][z][w] = 1;
            continue;
        }
        grid[x][y][z][w] = 0;
    }
}


int compute(grid_t grid) {
    for (int i = 0; i < CYCLES; i++)
        cycle(grid);

    int sum = 0;

    for (int x = 0; x < MAX; x++)
    for (int y = 0; y < MAX; y++)
    for (int z = 0; z < MAX; z++)
    for (int w = 0; w < MAX; w++)
        sum += grid[x][y][z][w];

    return sum;
}


int main(void) {
    char filename[50];

    size_t slash_idx = strlen(__FILE__) - 1;

    while (__FILE__[slash_idx] != '/')
        slash_idx--;

    strncpy(filename, __FILE__, slash_idx);
    strcat(filename, "/input.txt");

    FILE *file = fopen(filename, "r");
    grid_t grid = {0};

    char c;

    int x = INITIAL_ZERO;
    int y = INITIAL_ZERO;

    while ((c = fgetc(file)) != EOF) {
        if (c != '\n') {
            if (c == '#')
                grid[x][y][INITIAL_ZERO][INITIAL_ZERO] = 1;

            x++;
        } else {
            y++;
            x = INITIAL_ZERO;
        }
    }

    fclose(file);

    printf("%d\n", compute(grid));

    return 0;
}