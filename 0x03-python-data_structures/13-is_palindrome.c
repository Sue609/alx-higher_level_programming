#include "lists.h"
/**
 * is_palindrome - a function that checks if a number is a palinfrome.
 * @head: a double pointer
 *
 * Return: an integer 1 or 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *secondHalf = NULL, *prev = NULL, *temp = NULL;
	int isPalindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (isPalindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next; }
	if (fast != NULL)
	{
		secondHalf = slow->next;
		slow->next = NULL; }
	else
	{
		secondHalf = slow;
		prev->next = NULL; }
	while (secondHalf != NULL)
	{
		temp = secondHalf->next;
		prev = secondHalf;
		secondHalf = temp; }
	secondHalf = prev;
	temp = *head;
	while (secondHalf != NULL)
	{
		if (temp->n != secondHalf->n)
		{
			isPalindrome = 0;
			break; }
		temp = temp->next;
		secondHalf = secondHalf->next; }
	prev = NULL;
	while (*head != NULL)
	{
		temp = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = temp; }
	*head = prev;
	return (isPalindrome); }
