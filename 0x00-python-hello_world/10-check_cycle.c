#include "lists.h"
/**
 * check_cycle - checks for loop in linked list
 * @list: linked list
 *
 *
 * Return: 0 if no cycle 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t  *loop1 = list;
	listint_t *loop2 = list;



	while (loop1 && loop2 && loop2->next)
	{
		loop1 = loop1->next;
		loop2  = loop2->next->next;

		if (loop1 == loop2)
		{
			return (1);
		}
	}

	return (0);
}
