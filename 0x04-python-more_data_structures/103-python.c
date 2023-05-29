#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);


	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", 1, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	printf("[.] bytes objects info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);
	printf("  first %ld bytes:", (size < 10) ? size : 10);

	for (i = 0; i < 10 && i < size; i++)
	{
		printf(" %02hhx", bytes[i]);
	}

	printf("\n");
/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) 
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *bytes;
    
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);
    
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);
    printf("  first %ld bytes:", (size < 10) ? size : 10);
    
    for (i = 0; i < 10 && i < size; i++)
        printf(" %02hhx", bytes[i]);
    printf("\n");
}
