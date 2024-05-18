#pragma once

#include <cstddef>

namespace genuid {
void InitParameters();
[[nodiscard]] std::size_t GenerateUID();
} // namespace genuid
