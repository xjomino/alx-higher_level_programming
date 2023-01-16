#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    char *str;
    Py_ssize_t len;
    int status;

    if (PyUnicode_Check(p))
    {
        PyObject *temp_bytes = PyUnicode_AsEncodedString(p, "utf-8", "strict");
        if (temp_bytes != NULL)
        {
            status = PyBytes_AsStringAndSize(temp_bytes, &str, &len);
            if (status == -1)
            {
                fprintf(stderr, "Error getting string and size\n");
                return;
            }

            printf("[.] string object info\n");
            printf("  type : %s\n", Py_TYPE(p)->tp_name);
            printf("  length : %ld\n", len);
            printf("  value : %s\n", str);

            Py_DECREF(temp_bytes);
        }
        else
        {
            fprintf(stderr, "Error encoding string\n");
        }
    }
    else
    {
        fprintf(stderr, "Error: Not a string object\n");
    }
}
