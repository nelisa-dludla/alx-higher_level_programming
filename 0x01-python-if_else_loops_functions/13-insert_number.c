#include "lists.h"

/**
 * insert_node - Function inserts a number into a singly linked list
 * @head: Head node of a singly linked list
 * @number: Number to be inserted into singly linked list
 * Return: Address of new node (success) / NULL (fail)
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode, *current, *prev;

    newNode = (listint_t *)malloc(sizeof(listint_t));

    if (newNode == NULL)
        return NULL;

    newNode->n = number;
    newNode->next = NULL;

    current = *head;

    if (current == NULL || current->n >= number)
    {
        newNode->next = current;
        *head = newNode;
        return (newNode);
    }

    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    prev->next = newNode;
    newNode->next = current;
    return (newNode);
}
