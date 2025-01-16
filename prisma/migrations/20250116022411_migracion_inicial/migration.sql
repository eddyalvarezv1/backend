-- CreateEnum
CREATE TYPE "ClasesDeUsuario" AS ENUM ('ADMIN', 'USUARIO', 'MODERADOR');

-- CreateTable
CREATE TABLE "usuarios" (
    "id" SERIAL NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "tipo_usuario" "ClasesDeUsuario" DEFAULT 'USUARIO',
    "nombre" TEXT,
    "apellido" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "imagenes" (
    "id" SERIAL NOT NULL,
    "Path" TEXT NOT NULL,
    "Extension" TEXT NOT NULL,
    "Nombre" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "imagenes_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "equipos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "estadio" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "imagen_id" INTEGER NOT NULL,

    CONSTRAINT "equipos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "partidos" (
    "id" SERIAL NOT NULL,
    "fecha" DATE NOT NULL,
    "hora" TIME NOT NULL,
    "score_equipo_local" INTEGER,
    "score_equipo_visitante" INTEGER,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "equipo_local_id" INTEGER NOT NULL,
    "equipo_visitante_id" INTEGER NOT NULL,

    CONSTRAINT "partidos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_email_key" ON "usuarios"("email");

-- CreateIndex
CREATE UNIQUE INDEX "equipos_imagen_id_key" ON "equipos"("imagen_id");

-- AddForeignKey
ALTER TABLE "equipos" ADD CONSTRAINT "equipos_imagen_id_fkey" FOREIGN KEY ("imagen_id") REFERENCES "imagenes"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "partidos" ADD CONSTRAINT "partidos_equipo_local_id_fkey" FOREIGN KEY ("equipo_local_id") REFERENCES "equipos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "partidos" ADD CONSTRAINT "partidos_equipo_visitante_id_fkey" FOREIGN KEY ("equipo_visitante_id") REFERENCES "equipos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
