import { z } from "zod";
import { tipoUsuario } from "@prisma/client";

// Todos los valores son requeridos por defecto a no ser que coloquemos la propiedad 'optional()'

export const registrarUsuarioSerializer = z.object({
    email: z.string().email(),
    password: z.string().regex(""),
    tipoUsuario: z.enum([
        tipoUsuario.ADMIN,
        tipoUsuario.MODERADOR,
        tipoUsuario.USUARIO,
    ]),
    nombre: z.string().optional(),
    apellido: z.string().optional(),
});

