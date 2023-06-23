#include "lists.h"

/**
 * check_cycle - ...
 *
 * @list: ...
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp_node;

	tmp_node = list;
	while (tmp_node != NULL)
	{
		if (tmp_node->next != list)
			tmp_node = tmp_node->next;
		else
			return (1);
	}
	return (0);
}
