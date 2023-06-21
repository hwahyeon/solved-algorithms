#include <stdio.h>
#include <string.h>

struct KeyValue {
    const char* key;
    const char* value;
};

int main() {
    struct KeyValue dict[] = {
        {"SONGDO", "HIGHSCHOOL"},
        {"CODE", "MASTER"},
        {"2023", "0611"},
        {"ALGORITHM", "CONTEST"}
    };

    char input[10];

    scanf("%s", input);

    for (int i = 0; i < sizeof(dict) / sizeof(struct KeyValue); i++) {
        if (strcmp(dict[i].key, input) == 0) {
            printf("%s\n", dict[i].value);
            break;
        }
    }

    return 0;
}
