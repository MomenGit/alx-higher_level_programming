#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp_node;

	if (*head == NULL)
		return (add_nodeint_end(head, number));

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	tmp_node = *head;
	if (tmp_node->n > number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (tmp_node->next != NULL && tmp_node->next->n < number)
			tmp_node = tmp_node->next;
		new_node->next = tmp_node->next;
		tmp_node->next = new_node;
	}

	return (new_node);
}
