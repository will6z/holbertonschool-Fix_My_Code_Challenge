#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at a given index in a doubly linked list.
 * @head: Pointer to a pointer to the first node in the list.
 * @index: Index of the node to delete.
 * 
 * Return: 1 on success, -1 on failure.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *temp = *head;
    unsigned int i;

    if (*head == NULL)  // Empty list
        return (-1);

    /* Deleting the first node */
    if (index == 0)
    {
        *head = temp->next;
        if (*head != NULL)
            (*head)->prev = NULL;
        free(temp);
        return (1);
    }

    /* Traverse to the node to be deleted */
    for (i = 0; temp != NULL && i < index; i++)
        temp = temp->next;

    if (temp == NULL)  // Index out of range
        return (-1);

    /* Update the previous node's next pointer */
    if (temp->prev != NULL)
        temp->prev->next = temp->next;

    /* Update the next node's previous pointer */
    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    free(temp);  // Free the node
    return (1);
}

