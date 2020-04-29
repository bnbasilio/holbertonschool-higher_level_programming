#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the linked list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *temp = *head;

    if (!head)
        return NULL;

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else if (number < temp->n)
    {
        new->next = temp;
        *head = new;
    }
    else
    {
        while (temp->next && number > temp->next->n)
            temp = temp->next;
        new->next = temp->next;
        temp->next = new;
    }

    return (new);
}
