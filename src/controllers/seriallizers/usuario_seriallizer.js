import { z } from "zod";
import { ClasesDeUsuario } from "@prisma/client";

// Todos los valores son requeridos por defecto a no ser que coloquemos la propiedad 'optional()'

export const registrarUsuarioSerializer = z.object({
    email: z.string().email(),
    password: z.string().regex(
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!*&%?#])[A-Za-z\d@$!*&%?#]{8,}$/
    ),
    tipoUsuario: z.enum([
        ClasesDeUsuario.ADMIN,
        ClasesDeUsuario.MODERADOR,
        ClasesDeUsuario.USUARIO,
    ]),
    nombre: z.string().optional(),
    apellido: z.string().optional(),
});


export const loginSerializer =z.object({
    email: z.string().email(),
    password: z.string(),
});

