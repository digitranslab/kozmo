import { KozmoClient, BASE_URL, routes } from ".";

import axios from 'axios'

jest.mock('axios')

describe('Client', () => {
  let kozmoClient
  beforeEach(() => {
    kozmoClient = new KozmoClient('test')
  })

  test('should create a client', () => {
    expect(kozmoClient).toBeDefined();
  })
  // test updateApiKey
  test('should update the api key', () => {
    kozmoClient.updateApiKey('test2');
    expect(kozmoClient.apiKey).toBe('test2');
  })
});

describe('Send Requests', () => {
  let kozmoClient

  beforeEach(() => {
    kozmoClient = new KozmoClient('test')
  })

  afterEach(() => {
    jest.resetAllMocks()
  })

  it('should make a successful request to the application parameter', async () => {
    const method = 'GET'
    const endpoint = routes.application.url
    const expectedResponse = { data: 'response' }
    axios.mockResolvedValue(expectedResponse)

    await kozmoClient.sendRequest(method, endpoint)

    expect(axios).toHaveBeenCalledWith({
      method,
      url: `${BASE_URL}${endpoint}`,
      params: null,
      headers: {
        Authorization: `Bearer ${kozmoClient.apiKey}`,
        'Content-Type': 'application/json',
      },
      responseType: 'json',
    })

  })

  it('should handle errors from the API', async () => {
    const method = 'GET'
    const endpoint = '/test-endpoint'
    const errorMessage = 'Request failed with status code 404'
    axios.mockRejectedValue(new Error(errorMessage))

    await expect(kozmoClient.sendRequest(method, endpoint)).rejects.toThrow(
      errorMessage
    )
  })
})