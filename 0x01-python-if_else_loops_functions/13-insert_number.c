#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts a node at strigly linked list
 * @head: pointer to a pointer to the head of the list.
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
