gcc -I utilities -I linear-algebra/blas/gesummv utilities/polybench.c linear-algebra/blas/gesummv/gesummv.c -DPOLYBENCH_DUMP_ARRAYS -o gesummv 

