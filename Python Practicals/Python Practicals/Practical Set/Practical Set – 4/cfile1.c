#include <stdio.h>
#include <string.h>

void encryptRailFence(char *text, int key) {
    int len = strlen(text);
    char rail[key][len];
    memset(rail, 0, sizeof(rail));  // Initialize rail array with 0

    int row = 0, direction = 1;  // direction 1 means moving down, -1 means moving up

    // Fill rail matrix
    for (int i = 0; i < len; i++) {
        rail[row][i] = text[i];
        if (row == 0 || row == key - 1)
            direction = -direction; // Change direction
        row += direction;
    }

    // Print encrypted text by reading rail matrix row by row
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < len; j++) {
            if (rail[i][j] != 0)  // Print non-zero characters
                printf("%c", rail[i][j]);
        }
    }
    printf("\n");
}

void decryptRailFence(char *cipher, int key) {
    int len = strlen(cipher);
    char rail[key][len];
    memset(rail, 0, sizeof(rail));  // Initialize rail array with 0

    int row = 0, direction = 1;

    // Fill rail matrix
    for (int i = 0; i < len; i++) {
        rail[row][i] = '*'; // Mark all spots as filled
        if (row == 0 || row == key - 1)
            direction = -direction; // Change direction
        row += direction;
    }

    // Fill rail matrix with cipher text
    int index = 0;
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < len; j++) {
            if (rail[i][j] == '*' && index < len)
                rail[i][j] = cipher[index++];
        }
    }

    // Read the matrix and get the original message
    row = 0, direction = 1;
    for (int i = 0; i < len; i++) {
        printf("%c", rail[row][i]);
        if (row == 0 || row == key - 1)
            direction = -direction;
        row += direction;
    }
    printf("\n");
}

int main() {
    char text[100];
    int key;

    printf("Enter the text: ");
    gets(text);
    printf("Enter the key: ");
    scanf("%d", &key);

    printf("Encrypted text: ");
    encryptRailFence(text, key);

    printf("Decrypted text: ");
    decryptRailFence(text, key);

    return 0;
}
