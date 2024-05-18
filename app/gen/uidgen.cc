#include <nanobind/nanobind.h>

#include "genuid.hpp"

NB_MODULE(uidgen, m) {
  genuid::InitParameters();
  m.def("GenerateUID", &genuid::GenerateUID);
}
