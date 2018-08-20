import usermanage from '@/components/admin/usermanage'

describe('usermanage', () => {
  it('set a correct data', () => {
    expect(typeof usermanage.data).toBe('function')
    const defaultData = usermanage.data()
    expect(defaultData.userData[0].userName).toBe('zzgyy')
  })
})
