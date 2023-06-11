#include "lists.h"

/**
 * is_palind - A recursive function that compares
 * the poles of a linked list from outside in
 *
 * @head: the head of a linked list
 * @next_node: the next node of a linked list
 * Return: 1 if the poles match else returns 0
 */
int is_palind(listint_t **head, listint_t *next_node)
{
	if (next_node)
	{
		if (is_palind(head, next_node->next))
		{
			if ((*head)->n == next_node->n)
			{
				*head = ((*head)->next);
				return (1);
			}
		}
		return (0);
	}
	return (1);
}

/**
 * is_palindrome - checks that a linked list is a palindrome
 *
 * @head: the head of a linked list
 * Return: 1 if palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *head_cp;

	if (*head == NULL)
		return (1);

	head_cp = *head;
	return (is_palind(&head_cp, head_cp->next));
}
