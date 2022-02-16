import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Calendar from 'react-calendar';
import { useCallback, useEffect, useMemo, useState } from 'react';
import { Button, Card, Col, Container, Input, Row, Spacer, Text, Textarea } from '@nextui-org/react';
import moment from 'moment';

interface Journals {
  [key: string]: string;
}
const formatDate = (date: Date) => {
  return moment(date).format('YYYY-MM-DD');
}

const Home: NextPage = () => {

  const [date, setDate] = useState(formatDate(new Date()))
  const [journals, setJournals] = useState<Journals>({})
  const text = useMemo(() => journals[date] || '', [date, journals])

  const updateJournal = useCallback((text: string) => {
    setJournals({
      ...journals,
      [date]: text
    })
  }, [date])

  // Effect to load journals from local storage
  useEffect(() => {
    const journals = localStorage.getItem('journals')
    if (journals) {
      setJournals(JSON.parse(journals))
    }
  }, [])

  useEffect(() => {
    localStorage.setItem('journals', JSON.stringify(journals))
  }, [journals])

  useEffect(() => {
    console.log(date);
  }, [date])

  return (
    <Container css={{ height: '100vh' }} justify="center" direction="column" display="flex">
      <Head>
        <title>NLP Mood Journal</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Card css={{ height: '80%' }}>
        <Container gap={2} direction="column" display="flex" css={{ height: '100%' }}>
          <Row justify='center'>
            <Text h1>NLP Mood Journal</Text>
          </Row>
          <Spacer />
          <Row>
            <Col>
              <Text h3>
                Daily Journal for&nbsp;
                <Input type="date" value={date} size="xl" onChange={(e) => setDate(e.target.value)} />
              </Text>
            </Col>
            <Col>
              <Row justify='flex-end'>
                <Button onClick={() => updateJournal('')} color="error">Clear Journal</Button>
              </Row>
            </Col>
          </Row>
          <Spacer />
          <Row css={{ flexGrow: 1 }}>
            <Textarea value={text} fullWidth onChange={e => updateJournal(e.target.value)} size="xl" minRows={75} placeholder="Tell me about your day"></Textarea>
          </Row>
        </Container>
      </Card>
    </Container>
  )
}

export default Home
