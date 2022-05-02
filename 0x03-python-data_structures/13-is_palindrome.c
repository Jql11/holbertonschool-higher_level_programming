#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  *reverse - reverse list
  *@head: head
  */
void reverse(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prevNode = NULL, *nextNode = NULL;

	while (current != NULL)
	{
		nextNode = current->next;
		current->next = prevNode;
		prevNode = current;
		current = nextNode;
	}
	*head = prevNode;
}
/**
  *compareLists - check if two input lists have same data
  *@head1: head1
  *@head2: head2
  *Return: 0 false, 1 true
  */
int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
        listint_t *slow = *head, *fast = *head;
        listint_t *second_half, *prev_of_slow = *head;
        listint_t *midnode = NULL;
        int res;

        if (*head == NULL || (*head)->next != NULL)
        {
                while (fast != NULL && fast->next != NULL)
                {
                        fast = fast->next->next;
                        prev_of_slow = slow;
                        slow = slow->next;
                }
                if (fast != NULL)
                {
                        midnode = slow;
                        slow = slow->next;
                }
                second_half = slow;
                prev_of_slow->next = NULL;
                reverse(&second_half);
                res = compareLists(*head, second_half);

                reverse(&second_half);

                if (midnode != NULL)
                {
                        prev_of_slow->next = midnode;
                        midnode->next = second_half;
                }
                else
                        prev_of_slow->next = second_half;

        }
        return (res);
}
