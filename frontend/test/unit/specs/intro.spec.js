import intro from '@/components/user/intro'

describe('intro', () => {
  it('set a correct data', () => {
    expect(typeof intro.data).toBe('function')
    const defaultData = intro.data()
    expect(defaultData.title).toBe('我们爱科学')
  })
})
