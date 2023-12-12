SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;


CREATE TABLE public."OBJ_CONTA" (
    id integer NOT NULL,
    conta_id integer,
    saldo double precision,
    user_fk integer,
    is_active boolean,
    created timestamp without time zone
);


CREATE TABLE public."OBJ_EXTRATO" (
    id integer NOT NULL,
    conta_fk integer,
    forma_pgto character varying(1),
    saldo_anterior double precision,
    saldo_pos_transacao double precision,
    updated timestamp without time zone
);


CREATE TABLE public."OBJ_HASH" (
    id bigint NOT NULL,
    hash character varying,
    date timestamp without time zone
);


CREATE TABLE public."OBJ_USER" (
    id bigint NOT NULL,
    senha character varying(128) NOT NULL,
    ultimo_login timestamp without time zone,
    username character varying(150),
    nome character varying(150) NOT NULL,
    sobrenome character varying(150),
    email character varying(254) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp without time zone,
    log_user character varying
);


CREATE SEQUENCE public.obj_conta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.obj_conta_id_seq OWNED BY public."OBJ_CONTA".id;


CREATE SEQUENCE public.obj_extrato_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.obj_extrato_id_seq OWNED BY public."OBJ_EXTRATO".id;


CREATE SEQUENCE public.obj_hash_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.obj_hash_id_seq OWNED BY public."OBJ_HASH".id;


CREATE SEQUENCE public.obj_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.obj_user_id_seq OWNED BY public."OBJ_USER".id;


ALTER TABLE ONLY public."OBJ_CONTA" ALTER COLUMN id SET DEFAULT nextval('public.obj_conta_id_seq'::regclass);


ALTER TABLE ONLY public."OBJ_EXTRATO" ALTER COLUMN id SET DEFAULT nextval('public.obj_extrato_id_seq'::regclass);


ALTER TABLE ONLY public."OBJ_HASH" ALTER COLUMN id SET DEFAULT nextval('public.obj_hash_id_seq'::regclass);


ALTER TABLE ONLY public."OBJ_USER" ALTER COLUMN id SET DEFAULT nextval('public.obj_user_id_seq'::regclass);


SELECT pg_catalog.setval('public.obj_conta_id_seq', 1, true);


SELECT pg_catalog.setval('public.obj_extrato_id_seq', 1, false);


SELECT pg_catalog.setval('public.obj_hash_id_seq', 1, false);


SELECT pg_catalog.setval('public.obj_user_id_seq', 1, false);


ALTER TABLE ONLY public."OBJ_CONTA"
    ADD CONSTRAINT "OBJ_CONTA_pkey" PRIMARY KEY (id);


ALTER TABLE ONLY public."OBJ_EXTRATO"
    ADD CONSTRAINT "OBJ_EXTRATO_pkey" PRIMARY KEY (id);


ALTER TABLE ONLY public."OBJ_HASH"
    ADD CONSTRAINT "OBJ_HASH_pkey" PRIMARY KEY (id);


ALTER TABLE ONLY public."OBJ_USER"
    ADD CONSTRAINT "OBJ_USER_pkey" PRIMARY KEY (id);


