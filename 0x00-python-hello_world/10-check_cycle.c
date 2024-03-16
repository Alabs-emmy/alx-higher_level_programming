#include "list.h"

/**
 * check_cycle - checks cycle
 * @list: pointer to the  node
 *
 * Description: checks for cycle in a singly linked list
 *
 * Return: 0- if there is no cycle
 *         1- if there is cycle
 */


int check_cycle(listint_t *list)
{
	listint_t *check = NULL;

	if (list == NULL || list->next == NULL || (list->next)->next == NULL)
		return (0);
	check = (list->next)->next;

	while (list != NULL)
	{
		if (list == check)
			return (1);
		if (list != check)
		{
			if (check->next != NULL && (check->next)->next != NULL)
			{
				check = (check->next)->next;
			}
			else
				check = NULL;
		}
		list = list->next;
	}
	return (1);
}
