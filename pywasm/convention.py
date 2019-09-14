i32 = 0x7F
i64 = 0x7E
f32 = 0x7D
f64 = 0x7C

valtype = {i32: ["i32"], i64: ["i64"], f32: ["f32"], f64: ["f64"]}

empty = 0x40

blocktype = {empty: ["empty"], **valtype}

funcref = 0x70

elemtype = {funcref: ["funcref"]}


opcodes = {}


def op(code, name, code_size, load_size):
    opcodes[code] = (name, code_size, load_size)
    return code


# control Instructions
unreachable = op(0x00, "unreachable", "", 0)
nop = op(0x01, "nop", "", 0)
block = op(0x02, "block", "u8", 0)
loop = op(0x03, "loop", "u8", 0)
if_ = op(0x04, "if", "u8", 0)
else_ = op(0x05, "else", "", 0)
end = op(0x0B, "end", "", 0)
br = op(0x0C, "br", "u32", 0)
br_if = op(0x0D, "br_if", "u32", 0)
br_table = op(0x0E, "br_table", "complex", 0)
return_ = op(0x0F, "return", "", 0)
call = op(0x10, "call", "u32", 0)
call_indirect = op(0x11, "call_indirect", "u32,u8", 0)
# parametric Instructions
drop = op(0x1A, "drop", "", 0)
select = op(0x1B, "select", "", 0)
# variable instructions
get_local = op(0x20, "local.get", "u32", 0)
set_local = op(0x21, "local.set", "u32", 0)
tee_local = op(0x22, "local.tee", "u32", 0)
get_global = op(0x23, "global.get", "u32", 0)
set_global = op(0x24, "global.set", "u32", 0)
# memory instructions
i32_load = op(0x28, "i32.load", "u32,u32", 4)
i64_load = op(0x29, "i64.load", "u32,u32", 8)
f32_load = op(0x2A, "f32.load", "u32,u32", 4)
f64_load = op(0x2B, "f64.load", "u32,u32", 8)
i32_load8_s = op(0x2C, "i32.load8_s", "u32,u32", 1)
i32_load8_u = op(0x2D, "i32.load8_u", "u32,u32", 1)
i32_load16_s = op(0x2E, "i32.load16_s", "u32,u32", 2)
i32_load16_u = op(0x2F, "i32.load16_u", "u32,u32", 2)
i64_load8_s = op(0x30, "i64.load8_s", "u32,u32", 1)
i64_load8_u = op(0x31, "i64.load8_u", "u32,u32", 1)
i64_load16_s = op(0x32, "i64.load16_s", "u32,u32", 2)
i64_load16_u = op(0x33, "i64.load16_u", "u32,u32", 2)
i64_load32_s = op(0x34, "i64.load32_s", "u32,u32", 4)
i64_load32_u = op(0x35, "i64.load32_u", "u32,u32", 4)
i32_store = op(0x36, "i32.store", "u32,u32", 4)
i64_store = op(0x37, "i64.store", "u32,u32", 8)
f32_store = op(0x38, "f32.store", "u32,u32", 4)
f64_store = op(0x39, "f64.store", "u32,u32", 8)
i32_store8 = op(0x3A, "i32.store8", "u32,u32", 1)
i32_store16 = op(0x3B, "i32.store16", "u32,u32", 2)
i64_store8 = op(0x3C, "i64.store8", "u32,u32", 1)
i64_store16 = op(0x3D, "i64.store16", "u32,u32", 2)
i64_store32 = op(0x3E, "i64.store32", "u32,u32", 4)
current_memory = op(0x3F, "memory.size", "u8", 0)
grow_memory = op(0x40, "memory.grow", "u8", 1)
# numeric instructions
i32_const = op(0x41, "i32.const", "i32", 2)
i64_const = op(0x42, "i64.const", "i64", 1)
f32_const = op(0x43, "f32.const", "f32", 2)
f64_const = op(0x44, "f64.const", "f64", 4)
i32_eqz = op(0x45, "i32.eqz", "", 0)
i32_eq = op(0x46, "i32.eq", "", 0)
i32_ne = op(0x47, "i32.ne", "", 0)
i32_lts = op(0x48, "i32.lt_s", "", 0)
i32_ltu = op(0x49, "i32.lt_u", "", 0)
i32_gts = op(0x4A, "i32.gt_s", "", 0)
i32_gtu = op(0x4B, "i32.gt_u", "", 0)
i32_les = op(0x4C, "i32.le_s", "", 0)
i32_leu = op(0x4D, "i32.le_u", "", 0)
i32_ges = op(0x4E, "i32.ge_s", "", 0)
i32_geu = op(0x4F, "i32.ge_u", "", 0)
i64_eqz = op(0x50, "i64.eqz", "", 0)
i64_eq = op(0x51, "i64.eq", "", 0)
i64_ne = op(0x52, "i64.ne", "", 0)
i64_lts = op(0x53, "i64.lt_s", "", 0)
i64_ltu = op(0x54, "i64.lt_u", "", 0)
i64_gts = op(0x55, "i64.gt_s", "", 0)
i64_gtu = op(0x56, "i64.gt_u", "", 0)
i64_les = op(0x57, "i64.le_s", "", 0)
i64_leu = op(0x58, "i64.le_u", "", 0)
i64_ges = op(0x59, "i64.ge_s", "", 0)
i64_geu = op(0x5A, "i64.ge_u", "", 0)
f32_eq = op(0x5B, "f32.eq", "", 0)
f32_ne = op(0x5C, "f32.ne", "", 0)
f32_lt = op(0x5D, "f32.lt", "", 0)
f32_gt = op(0x5E, "f32.gt", "", 0)
f32_le = op(0x5F, "f32.le", "", 0)
f32_ge = op(0x60, "f32.ge", "", 0)
f64_eq = op(0x61, "f64.eq", "", 0)
f64_ne = op(0x62, "f64.ne", "", 0)
f64_lt = op(0x63, "f64.lt", "", 0)
f64_gt = op(0x64, "f64.gt", "", 0)
f64_le = op(0x65, "f64.le", "", 0)
f64_ge = op(0x66, "f64.ge", "", 0)
i32_clz = op(0x67, "i32.clz", "", 0)
i32_ctz = op(0x68, "i32.ctz", "", 0)
i32_popcnt = op(0x69, "i32.popcnt", "", 0)
i32_add = op(0x6A, "i32.add", "", 0)
i32_sub = op(0x6B, "i32.sub", "", 0)
i32_mul = op(0x6C, "i32.mul", "", 0)
i32_divs = op(0x6D, "i32.div_s", "", 0)
i32_divu = op(0x6E, "i32.div_u", "", 0)
i32_rems = op(0x6F, "i32.rem_s", "", 0)
i32_remu = op(0x70, "i32.rem_u", "", 0)
i32_and = op(0x71, "i32.and", "", 0)
i32_or = op(0x72, "i32.or", "", 0)
i32_xor = op(0x73, "i32.xor", "", 0)
i32_shl = op(0x74, "i32.shl", "", 0)
i32_shrs = op(0x75, "i32.shr_s", "", 0)
i32_shru = op(0x76, "i32.shr_u", "", 0)
i32_rotl = op(0x77, "i32.rotl", "", 0)
i32_rotr = op(0x78, "i32.rotr", "", 0)
i64_clz = op(0x79, "i64.clz", "", 0)
i64_ctz = op(0x7A, "i64.ctz", "", 0)
i64_popcnt = op(0x7B, "i64.popcnt", "", 0)
i64_add = op(0x7C, "i64.add", "", 0)
i64_sub = op(0x7D, "i64.sub", "", 0)
i64_mul = op(0x7E, "i64.mul", "", 0)
i64_divs = op(0x7F, "i64.div_s", "", 0)
i64_divu = op(0x80, "i64.div_u", "", 0)
i64_rems = op(0x81, "i64.rem_s", "", 0)
i64_remu = op(0x82, "i64.rem_u", "", 0)
i64_and = op(0x83, "i64.and", "", 0)
i64_or = op(0x84, "i64.or", "", 0)
i64_xor = op(0x85, "i64.xor", "", 0)
i64_shl = op(0x86, "i64.shl", "", 0)
i64_shrs = op(0x87, "i64.shr_s", "", 0)
i64_shru = op(0x88, "i64.shr_u", "", 0)
i64_rotl = op(0x89, "i64.rotl", "", 0)
i64_rotr = op(0x8A, "i64.rotr", "", 0)
f32_abs = op(0x8B, "f32.abs", "", 0)
f32_neg = op(0x8C, "f32.neg", "", 0)
f32_ceil = op(0x8D, "f32.ceil", "", 0)
f32_floor = op(0x8E, "f32.floor", "", 0)
f32_trunc = op(0x8F, "f32.trunc", "", 0)
f32_nearest = op(0x90, "f32.nearest", "", 0)
f32_sqrt = op(0x91, "f32.sqrt", "", 0)
f32_add = op(0x92, "f32.add", "", 0)
f32_sub = op(0x93, "f32.sub", "", 0)
f32_mul = op(0x94, "f32.mul", "", 0)
f32_div = op(0x95, "f32.div", "", 0)
f32_min = op(0x96, "f32.min", "", 0)
f32_max = op(0x97, "f32.max", "", 0)
f32_copysign = op(0x98, "f32.copysign", "", 0)
f64_abs = op(0x99, "f64.abs", "", 0)
f64_neg = op(0x9A, "f64.neg", "", 0)
f64_ceil = op(0x9B, "f64.ceil", "", 0)
f64_floor = op(0x9C, "f64.floor", "", 0)
f64_trunc = op(0x9D, "f64.trunc", "", 0)
f64_nearest = op(0x9E, "f64.nearest", "", 0)
f64_sqrt = op(0x9F, "f64.sqrt", "", 0)
f64_add = op(0xA0, "f64.add", "", 0)
f64_sub = op(0xA1, "f64.sub", "", 0)
f64_mul = op(0xA2, "f64.mul", "", 0)
f64_div = op(0xA3, "f64.div", "", 0)
f64_min = op(0xA4, "f64.min", "", 0)
f64_max = op(0xA5, "f64.max", "", 0)
f64_copysign = op(0xA6, "f64.copysign", "", 0)
i32_wrap_i64 = op(0xA7, "i32.wrap_i64", "", 0)
i32_trunc_sf32 = op(0xA8, "i32.trunc_f32_s", "", 0)
i32_trunc_uf32 = op(0xA9, "i32.trunc_f32_u", "", 0)
i32_trunc_sf64 = op(0xAA, "i32.trunc_f64_s", "", 0)
i32_trunc_uf64 = op(0xAB, "i32.trunc_f64_u", "", 0)
i64_extend_si32 = op(0xAC, "i64.extend_i32_s", "", 0)
i64_extend_ui32 = op(0xAD, "i64.extend_i32_u", "", 0)
i64_trunc_sf32 = op(0xAE, "i64.trunc_f32_s", "", 0)
i64_trunc_uf32 = op(0xAF, "i64.trunc_f32_u", "", 0)
i64_trunc_sf64 = op(0xB0, "i64.trunc_f64_s", "", 0)
i64_trunc_uf64 = op(0xB1, "i64.trunc_f64_u", "", 0)
f32_convert_si32 = op(0xB2, "f32.convert_i32_s", "", 0)
f32_convert_ui32 = op(0xB3, "f32.convert_i32_u", "", 0)
f32_convert_si64 = op(0xB4, "f32.convert_i64_s", "", 0)
f32_convert_ui64 = op(0xB5, "f32.convert_i64_u", "", 0)
f32_demote_f64 = op(0xB6, "f32.demote_f64", "", 0)
f64_convert_si32 = op(0xB7, "f64.convert_i32_s", "", 0)
f64_convert_ui32 = op(0xB8, "f64.convert_i32_u", "", 0)
f64_convert_si64 = op(0xB9, "f64.convert_i64_s", "", 0)
f64_convert_ui64 = op(0xBA, "f64.convert_i64_u", "", 0)
f64_promote_f32 = op(0xBB, "f64.promote_f32", "", 0)
i32_reinterpret_f32 = op(0xBC, "i32.reinterpret_f32", "", 0)
i64_reinterpret_f64 = op(0xBD, "i64.reinterpret_f64", "", 0)
f32_reinterpret_i32 = op(0xBE, "f32.reinterpret_i32", "", 0)
f64_reinterpret_i64 = op(0xBF, "f64.reinterpret_i64", "", 0)

custom_section = 0x00
type_section = 0x01
import_section = 0x02
function_section = 0x03
table_section = 0x04
memory_section = 0x05
global_section = 0x06
export_section = 0x07
start_section = 0x08
element_section = 0x09
code_section = 0x0A
data_section = 0x0B

section = {
    custom_section: ["Custom"],
    type_section: ["Type"],
    import_section: ["Import"],
    function_section: ["Function"],
    table_section: ["Table"],
    memory_section: ["Memory"],
    global_section: ["Global"],
    export_section: ["Export"],
    start_section: ["Start"],
    element_section: ["Element"],
    code_section: ["Code"],
    data_section: ["Data"],
}

extern_func = 0x00
extern_table = 0x01
extern_mem = 0x02
extern_global = 0x03

extern_type = {
    extern_func: ["func"],
    extern_table: ["table"],
    extern_mem: ["mem"],
    extern_global: ["global"],
}

section_code_to_name = {
    globals()[s]: s.split("_", 1)[0]
    for s in dir()
    if s.count("_") == 1 and s.endswith("_section")
}
