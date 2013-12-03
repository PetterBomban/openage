#ifndef _ENGINE_COORD_VEC3F_H_
#define _ENGINE_COORD_VEC3F_H_

#include "decl.h"

#define MEMBERS x, y, z
#define SCALAR_TYPE float
#define ABSOLUTE_TYPE vec3f
#define RELATIVE_TYPE vec3f_delta

namespace engine {
namespace coord {

struct vec3f {
	float x, y, z;

	#include "ops/abs.h"
};

struct vec3f_delta {
	float x, y, z;

	#include "ops/rel.h"
};

#include "ops/free.h"

#ifdef GEN_IMPL_VEC3F_CPP
#include "ops/impl.h"
#endif //GEN_IMPL_VEC3F_CPP

} //namespace coord
} //namespace engine

#undef MEMBERS
#undef RELATIVE_TYPE
#undef ABSOLUTE_TYPE
#undef SCALAR_TYPE

#endif //_ENGINE_COORD_VEC3F_H_
