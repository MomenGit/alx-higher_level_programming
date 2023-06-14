#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints prints some basic info about Python lists
 *
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len = 0;

	if (!PyList_Check(p))
		return;

	list_len = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", list_len);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < list_len; i++)
	{
		printf("Element %li: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - print some info about Python Python bytes objects
 *
 * @p: python object
 */
void print_python_bytes(PyObject *p) {}