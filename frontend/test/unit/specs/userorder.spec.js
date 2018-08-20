import userorder from '@/components/user/userorder'

describe('userorder', () => {
  it('set a correct data', () => {
    expect(typeof userorder.data).toBe('function')
    const defaultData = userorder.data()
    expect(defaultData.userOrderList[0].order_id).toBe('110')
  })
})
