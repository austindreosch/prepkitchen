--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

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
-- Name: orders; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    user_id integer,
    plan_id integer,
    date timestamp without time zone NOT NULL,
    billing_name text NOT NULL,
    billing_card text NOT NULL,
    billing_code text NOT NULL,
    billing_street text NOT NULL,
    billing_city text NOT NULL,
    billing_state text NOT NULL,
    billing_zip text NOT NULL,
    price double precision NOT NULL,
    tax double precision NOT NULL,
    total double precision NOT NULL,
    meal_id1 integer NOT NULL,
    meal_id2 integer NOT NULL,
    meal_id3 integer NOT NULL,
    meal_id4 integer,
    meal_id5 integer
);


--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: plans; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.plans (
    id integer NOT NULL,
    price double precision NOT NULL,
    serving_count integer NOT NULL,
    meal_count integer NOT NULL,
    image_url text NOT NULL,
    active boolean
);


--
-- Name: plans_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.plans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: plans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.plans_id_seq OWNED BY public.plans.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL,
    address_street text NOT NULL,
    address_city text NOT NULL,
    address_state text NOT NULL,
    address_zip text NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: plans id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plans ALTER COLUMN id SET DEFAULT nextval('public.plans_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.orders (id, user_id, plan_id, date, billing_name, billing_card, billing_code, billing_street, billing_city, billing_state, billing_zip, price, tax, total, meal_id1, meal_id2, meal_id3, meal_id4, meal_id5) FROM stdin;
1	1	1	2023-06-24 05:56:54.081836	John Doe	1234567890123456	123	123 Main St	San Francisco	CA	12345	29.99	0	29.99	53036	52895	53041	\N	\N
2	1	2	2023-06-24 05:57:00.94782	austin dreosch	1231231243rfdf	323	1410 Hughes Ave	Santa Rosa	CA	95407	49.99	3.63	53.62	53036	53044	52847	52999	52885
3	1	3	2023-06-24 06:02:43.235779	austin d	10298319283	098	1410 Hughes Ave	Santa Rosa	CA	95407	64.99	4.72	69.71	53018	52847	52822	52994	\N
4	2	1	2023-07-18 06:26:28.691586	Austin Dreosch	489639852	123	1410 Hughes Ave	Santa Rosa	CA	95407	29.99	2.18	32.17	53018	52999	52994	\N	\N
5	2	1	2023-07-18 06:26:28.691586	austin dreosch	12356768678	123	1410 Hughes Ave	Santa Rosa	CA	95407	29.99	2.18	32.17	53036	53035	52994	\N	\N
\.


--
-- Data for Name: plans; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.plans (id, price, serving_count, meal_count, image_url, active) FROM stdin;
1	29.99	2	3	https://i.postimg.cc/5fBHLzDx/plan1.png	t
2	49.99	2	5	https://i.postimg.cc/VsymZ8ZJ/plan2.png	t
3	64.99	4	4	https://i.postimg.cc/wznqjXx9/plan3.png	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, username, password, first_name, last_name, email, address_street, address_city, address_state, address_zip) FROM stdin;
1	adreosch21	$2b$12$KXD0bLNMS5pk2C.WTIr7Y.Oc7GiNPliUB5BKmp1uYIpDslI7OSFKm	Austin	Dreosch	austindreosch@gmail.com	234 Westgate St.	San Vicardo	CA	84561
2	adreosch	$2b$12$zLmtIPJvWGCf.JGVoQcyG.2zuviy8LhnkMwgdpExXnkZRVx7OYYkS	Austin	Dreosch	austindreosch2@gmail.com	9219 Anderson Mill Rd. #1032	Austin	TX	78729
\.


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.orders_id_seq', 5, true);


--
-- Name: plans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.plans_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: plans plans_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plans
    ADD CONSTRAINT plans_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: orders orders_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_plan_id_fkey FOREIGN KEY (plan_id) REFERENCES public.plans(id);


--
-- Name: orders orders_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

