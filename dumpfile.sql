--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: book_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book_types (
    id integer NOT NULL,
    subject_name character varying
);


ALTER TABLE public.book_types OWNER TO postgres;

--
-- Name: book_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.book_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_types_id_seq OWNER TO postgres;

--
-- Name: book_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.book_types_id_seq OWNED BY public.book_types.id;


--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name character varying,
    author character varying,
    copy_number integer,
    book_type_id integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: borrows; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.borrows (
    id integer NOT NULL,
    student_id integer,
    book_id integer
);


ALTER TABLE public.borrows OWNER TO postgres;

--
-- Name: borrows_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.borrows_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.borrows_id_seq OWNER TO postgres;

--
-- Name: borrows_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.borrows_id_seq OWNED BY public.borrows.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name character varying,
    department character varying
);


ALTER TABLE public.students OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: book_types id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book_types ALTER COLUMN id SET DEFAULT nextval('public.book_types_id_seq'::regclass);


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: borrows id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrows ALTER COLUMN id SET DEFAULT nextval('public.borrows_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Data for Name: book_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book_types (id, subject_name) FROM stdin;
1	Mathematics
2	Literature
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books (id, name, author, copy_number, book_type_id) FROM stdin;
3	Math 101	Math Guru	10	\N
4	Shakespeare Works	William Shakespeare	5	2
1	Guns	Jared Diamond	4	1
\.


--
-- Data for Name: borrows; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.borrows (id, student_id, book_id) FROM stdin;
5	1	3
6	3	4
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (id, name, department) FROM stdin;
1	John Doe	Computer Science
2	John Doe	Computer Science
3	Jane Doe	Physics
\.


--
-- Name: book_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.book_types_id_seq', 2, true);


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.books_id_seq', 4, true);


--
-- Name: borrows_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.borrows_id_seq', 6, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 3, true);


--
-- Name: book_types book_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book_types
    ADD CONSTRAINT book_types_pkey PRIMARY KEY (id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: borrows borrows_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrows
    ADD CONSTRAINT borrows_pkey PRIMARY KEY (id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: ix_book_types_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_book_types_id ON public.book_types USING btree (id);


--
-- Name: ix_books_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_books_id ON public.books USING btree (id);


--
-- Name: ix_borrows_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_borrows_id ON public.borrows USING btree (id);


--
-- Name: ix_students_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_students_id ON public.students USING btree (id);


--
-- Name: books books_book_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_book_type_id_fkey FOREIGN KEY (book_type_id) REFERENCES public.book_types(id);


--
-- Name: borrows borrows_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrows
    ADD CONSTRAINT borrows_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: borrows borrows_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrows
    ADD CONSTRAINT borrows_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id);


--
-- PostgreSQL database dump complete
--

