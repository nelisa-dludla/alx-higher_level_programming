#include "lists.h"

/**
* check_cycle - Function checks if a singly list has a cycle in it
* @list: Head of a singly linked list
* Return: 0 (Has no a cycle) / 1 (Has a cycle)
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
